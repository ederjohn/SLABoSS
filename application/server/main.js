import { Meteor } from 'meteor/meteor';

Meteor.startup(() => {
  // code to run on server at startup
});

Meteor.publish("myuser",
  function () {
    return Meteor.users.find(this.userId,
      {fields: {createdAt: 1}});
  }
);

