import admin from 'firebase-admin'
import serviceAccount from './firebase-service-account.json'

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: process.env.FIREBASE_DATABASE_URL
})

export const db = admin.firestore()
export const auth = admin.auth()
export const storage = admin.storage()

export const getDocument = async (collection, docId) => {
  const doc = await db.collection(collection).doc(docId).get()
  return doc.exists ? doc.data() : null
}

export const setDocument = async (collection, docId, data) => {
  await db.collection(collection).doc(docId).set(data)
}
