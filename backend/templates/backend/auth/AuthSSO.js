// Single Sign-On
import saml from 'passport-saml'

export const samlStrategy = new saml.Strategy({
    entryPoint: process.env.SAML_ENTRY_POINT,
    issuer: process.env.SAML_ISSUER,
    callbackUrl: process.env.SAML_CALLBACK_URL,
    cert: process.env.SAML_CERT
  },
  async (profile, done) => {
    try {
      let user = await User.findOne({ email: profile.email })

      if (!user) {
        user = await User.create({
          email: profile.email,
          name: profile.displayName,
          ssoId: profile.nameID
        })
      }

      return done(null, user)
    } catch (error) {
      return done(error, null)
    }
  }
)