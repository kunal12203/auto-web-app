"""
Payment Gateway Templates
Supports: Stripe, PayPal, Razorpay
"""

PAYMENT_GATEWAYS = {
    "stripe": {
        "name": "Stripe",
        "description": "Popular payment gateway with excellent documentation",
        "requires_backend": True,
        "env_vars": ["STRIPE_PUBLISHABLE_KEY", "STRIPE_SECRET_KEY", "STRIPE_WEBHOOK_SECRET"],
        "frontend_component": """
// Stripe Payment Component
import { useState } from 'react';
import { loadStripe } from '@stripe/stripe-js';
import { Elements, CardElement, useStripe, useElements } from '@stripe/react-stripe-js';

const stripePromise = loadStripe(import.meta.env.VITE_STRIPE_PUBLISHABLE_KEY);

function CheckoutForm() {
  const stripe = useStripe();
  const elements = useElements();
  const [error, setError] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [succeeded, setSucceeded] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setProcessing(true);

    if (!stripe || !elements) {
      return;
    }

    const cardElement = elements.getElement(CardElement);

    // Create payment intent
    const response = await fetch('/api/create-payment-intent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: 5000 }), // Amount in cents
    });

    const { clientSecret } = await response.json();

    const payload = await stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: cardElement,
      },
    });

    if (payload.error) {
      setError(`Payment failed: ${payload.error.message}`);
      setProcessing(false);
    } else {
      setError(null);
      setSucceeded(true);
      setProcessing(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="payment-form">
      <CardElement
        options={{
          style: {
            base: {
              fontSize: '16px',
              color: '#424770',
              '::placeholder': { color: '#aab7c4' },
            },
            invalid: { color: '#9e2146' },
          },
        }}
      />
      {error && <div className="error-message">{error}</div>}
      <button disabled={!stripe || processing || succeeded}>
        {processing ? 'Processing...' : 'Pay Now'}
      </button>
      {succeeded && <div className="success-message">Payment successful!</div>}
    </form>
  );
}

export default function StripePayment() {
  return (
    <Elements stripe={stripePromise}>
      <CheckoutForm />
    </Elements>
  );
}
""",
        "backend_route": """
# Stripe Backend Routes (FastAPI)
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import stripe
import os

router = APIRouter()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

class PaymentIntentRequest(BaseModel):
    amount: int  # Amount in cents

@router.post("/create-payment-intent")
async def create_payment_intent(request: PaymentIntentRequest):
    try:
        intent = stripe.PaymentIntent.create(
            amount=request.amount,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        return {"clientSecret": intent.client_secret}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, webhook_secret
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Handle the event
    if event["type"] == "payment_intent.succeeded":
        payment_intent = event["data"]["object"]
        print(f"Payment succeeded: {payment_intent['id']}")

    return {"status": "success"}
""",
        "dependencies": {
            "frontend": ["@stripe/stripe-js", "@stripe/react-stripe-js"],
            "backend": ["stripe"]
        }
    },

    "paypal": {
        "name": "PayPal",
        "description": "Widely used payment platform worldwide",
        "requires_backend": True,
        "env_vars": ["PAYPAL_CLIENT_ID", "PAYPAL_CLIENT_SECRET", "PAYPAL_MODE"],
        "frontend_component": """
// PayPal Payment Component
import { PayPalScriptProvider, PayPalButtons } from "@paypal/react-paypal-js";
import { useState } from 'react';

export default function PayPalPayment() {
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(false);

  const initialOptions = {
    "client-id": import.meta.env.VITE_PAYPAL_CLIENT_ID,
    currency: "USD",
    intent: "capture",
  };

  const createOrder = async () => {
    const response = await fetch('/api/paypal/create-order', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: 50.00 }),
    });
    const data = await response.json();
    return data.id;
  };

  const onApprove = async (data) => {
    const response = await fetch('/api/paypal/capture-order', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ orderID: data.orderID }),
    });
    const details = await response.json();
    setSuccess(true);
    console.log('Payment captured:', details);
  };

  return (
    <div className="paypal-payment">
      <PayPalScriptProvider options={initialOptions}>
        <PayPalButtons
          createOrder={createOrder}
          onApprove={onApprove}
          onError={(err) => setError(err.message)}
          style={{ layout: "vertical" }}
        />
      </PayPalScriptProvider>
      {error && <div className="error-message">{error}</div>}
      {success && <div className="success-message">Payment successful!</div>}
    </div>
  );
}
""",
        "backend_route": """
# PayPal Backend Routes (FastAPI)
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
import os
import base64

router = APIRouter()

PAYPAL_API = "https://api-m.sandbox.paypal.com" if os.getenv("PAYPAL_MODE") == "sandbox" else "https://api-m.paypal.com"

class PayPalOrderRequest(BaseModel):
    amount: float

class PayPalCaptureRequest(BaseModel):
    orderID: str

async def get_paypal_access_token():
    client_id = os.getenv("PAYPAL_CLIENT_ID")
    client_secret = os.getenv("PAYPAL_CLIENT_SECRET")

    auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API}/v1/oauth2/token",
            headers={
                "Authorization": f"Basic {auth}",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data={"grant_type": "client_credentials"}
        )
        return response.json()["access_token"]

@router.post("/create-order")
async def create_paypal_order(request: PayPalOrderRequest):
    access_token = await get_paypal_access_token()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API}/v2/checkout/orders",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            },
            json={
                "intent": "CAPTURE",
                "purchase_units": [{
                    "amount": {
                        "currency_code": "USD",
                        "value": str(request.amount)
                    }
                }]
            }
        )
        return response.json()

@router.post("/capture-order")
async def capture_paypal_order(request: PayPalCaptureRequest):
    access_token = await get_paypal_access_token()

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{PAYPAL_API}/v2/checkout/orders/{request.orderID}/capture",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
        )
        return response.json()
""",
        "dependencies": {
            "frontend": ["@paypal/react-paypal-js"],
            "backend": ["httpx"]
        }
    },

    "razorpay": {
        "name": "Razorpay",
        "description": "Popular payment gateway in India",
        "requires_backend": True,
        "env_vars": ["RAZORPAY_KEY_ID", "RAZORPAY_KEY_SECRET"],
        "frontend_component": """
// Razorpay Payment Component
import { useState } from 'react';

export default function RazorpayPayment() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const loadRazorpay = () => {
    return new Promise((resolve) => {
      const script = document.createElement('script');
      script.src = 'https://checkout.razorpay.com/v1/checkout.js';
      script.onload = () => resolve(true);
      script.onerror = () => resolve(false);
      document.body.appendChild(script);
    });
  };

  const handlePayment = async () => {
    setLoading(true);

    const res = await loadRazorpay();
    if (!res) {
      setError('Razorpay SDK failed to load');
      setLoading(false);
      return;
    }

    // Create order
    const response = await fetch('/api/razorpay/create-order', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount: 50000 }), // Amount in paise (50000 = ₹500)
    });
    const order = await response.json();

    const options = {
      key: import.meta.env.VITE_RAZORPAY_KEY_ID,
      amount: order.amount,
      currency: order.currency,
      name: 'Your Company',
      description: 'Product Purchase',
      order_id: order.id,
      handler: async function (response) {
        // Verify payment
        const verifyResponse = await fetch('/api/razorpay/verify-payment', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            razorpay_order_id: response.razorpay_order_id,
            razorpay_payment_id: response.razorpay_payment_id,
            razorpay_signature: response.razorpay_signature,
          }),
        });
        const result = await verifyResponse.json();
        if (result.verified) {
          alert('Payment successful!');
        } else {
          setError('Payment verification failed');
        }
        setLoading(false);
      },
      prefill: {
        name: 'Customer Name',
        email: 'customer@example.com',
        contact: '9999999999',
      },
      theme: {
        color: '#667eea',
      },
    };

    const paymentObject = new window.Razorpay(options);
    paymentObject.open();
    setLoading(false);
  };

  return (
    <div className="razorpay-payment">
      <button onClick={handlePayment} disabled={loading}>
        {loading ? 'Loading...' : 'Pay with Razorpay'}
      </button>
      {error && <div className="error-message">{error}</div>}
    </div>
  );
}
""",
        "backend_route": """
# Razorpay Backend Routes (FastAPI)
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import razorpay
import hmac
import hashlib
import os

router = APIRouter()

client = razorpay.Client(
    auth=(os.getenv("RAZORPAY_KEY_ID"), os.getenv("RAZORPAY_KEY_SECRET"))
)

class RazorpayOrderRequest(BaseModel):
    amount: int  # Amount in paise

class RazorpayVerifyRequest(BaseModel):
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str

@router.post("/create-order")
async def create_razorpay_order(request: RazorpayOrderRequest):
    try:
        order = client.order.create({
            "amount": request.amount,
            "currency": "INR",
            "payment_capture": 1
        })
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/verify-payment")
async def verify_razorpay_payment(request: RazorpayVerifyRequest):
    try:
        # Verify signature
        secret = os.getenv("RAZORPAY_KEY_SECRET")
        message = f"{request.razorpay_order_id}|{request.razorpay_payment_id}"
        generated_signature = hmac.new(
            secret.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()

        if generated_signature == request.razorpay_signature:
            return {"verified": True, "message": "Payment verified successfully"}
        else:
            return {"verified": False, "message": "Signature verification failed"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
""",
        "dependencies": {
            "frontend": [],  # Uses CDN
            "backend": ["razorpay"]
        }
    }
}

def get_payment_gateway_template(gateway_name: str):
    """Get payment gateway template by name"""
    return PAYMENT_GATEWAYS.get(gateway_name.lower())

def detect_payment_need(prompt: str) -> bool:
    """Detect if prompt mentions payment/checkout/purchase"""
    keywords = [
        'payment', 'checkout', 'purchase', 'buy', 'cart',
        'ecommerce', 'e-commerce', 'shop', 'store', 'subscription',
        'stripe', 'paypal', 'razorpay', 'billing'
    ]
    prompt_lower = prompt.lower()
    return any(keyword in prompt_lower for keyword in keywords)
