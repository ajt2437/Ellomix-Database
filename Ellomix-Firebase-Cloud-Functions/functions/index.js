// The Cloud Functions for Firebase SDK to create Cloud Functions and setup triggers.
const functions = require('firebase-functions');

// The Firebase Admin SDK to access the Firebase Realtime Database
const admin = require('firebase-admin');
admin.initializeApp();

// // Create and Deploy Your First Cloud Functions
// // https://firebase.google.com/docs/functions/write-firebase-functions
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//  response.send("Hello from Firebase!");
// });

// Listens for new groups added to /Messages/
exports.sendNewGroupNotification = functions.database.ref('/Groups/{groupId}')
    .onCreate((snapshot, context) => {
        //The topic name can be optionally prefixed with "/topics/"
        var topic = snapshot.key;

        var db = admin.database();

        //Subscribe all members to topic
        //1. Get list of group members' uuid
        var groupUsersSnapshot = snapshot.child("users");
        var membersList = groupUsersSnapshot.val();

        var registrationTokens = [];

        var userRef = db.ref("/Users");

        ref.once("value",
            (snapshot) => {
                for (memberUUID in membersList) {
                    //2. Get each user's registration token (aka Instance ID) from users ref

                    var registrationToken = snapshot.child(memberUUID).child("instance_ID").val();

                    if (registrationID !== undefined) {
                        registrationTokens.push(registrationToken);
                    }
                }
            },
            (error) => {
                console.log('Error value obtain message:', error);
                return false;
            });

        //3. Subscribe all user instance ID to the groud ID topic
        admin.messaging().subscribeToTopic(registrationTokens, topic)
            .then((response) => {
                //Response is a message
                console.log('Successfully subscribe users', response);
                return true;
            })
            .catch((error) => {
                console.log('Error subscribe users message:', error);
                return false;
            });



        var groupUsersRef = db.ref("/Groups/" + topic + "/users");


        //Print out group key
        console.log('Group key', topic);

        //Prepare message
        var message = {
            notification: {
                title: 'You just got invited to a new chat',
                body: 'Start chatting up'
            },
            topic: topic
        };

        //Send a message to devices subscribed to the provided topic
        admin.messaging().send(message)
            .then((response) => {
                //Response is a message
                console.log('Successfully sent message:', response);
                return true;
            })
            .catch((error) => {
                console.log('Error sending message:', error);
                return false;
            });
    });

exports.sendNewMessageNotification = functions.database.ref('/Messages/{groupId}/{messageId}')
    .onCreate((snapshot, context) => {

    });




// Listens for new messages added to /messages/:pushId/original and creates an
// uppercase version of the message to /messages/:pushId/uppercase
//exports.makeUppercase = functions.database.ref('/tests/{pushId}/original')
//    .onCreate((snapshot, context) => {
// Grab the current value of what was written to the Realtime Database.
//	    const original = snapshot.val();
//	    console.log('Uppercasing', context.params.pushId, original);
//	    const uppercase = original.toUpperCase();
// You must return a Promise when performing asynchronous tasks inside a Functions such as
// writing to the Firebase Realtime Database.
// Setting an "uppercase" sibling in the Realtime Database returns a Promise.
//	    return snapshot.ref.parent.child('uppercase').set(uppercase);
//	});