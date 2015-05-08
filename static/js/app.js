Groups = Ember.Application.create();

Groups.ApplicationAdapter = DS.RESTAdapter.extend({
  namespace: 'api/v1'
});

Groups.Router.map(function () {
  this.resource('groups', { path: '/' }, function () {  
    this.route('active');
    this.route('completed');
  });
});

Groups.GroupsRoute = Ember.Route.extend({
  model: function () {
    return this.store.find('group');
  }
});

Groups.GroupsIndexRoute = Ember.Route.extend({
  model: function () {
    return this.modelFor('groups');
  }
});

Groups.GroupsActiveRoute = Ember.Route.extend({
  model: function(){
    return this.store.filter('group', function (group) {
      return group.get('status') == 10;
    });
  },
  renderTemplate: function(controller){
    this.render('groups/index', {controller: controller});
  }
});

Groups.GroupsCompletedRoute = Ember.Route.extend({
  model: function(){
    return this.store.filter('group', function (group) {
      return group.get('status') != 10;
    });
  },
  renderTemplate: function(controller){
    this.render('groups/index', {controller: controller});
  }
});

Groups.Group = DS.Model.extend({
  id: DS.attr,
  title: DS.attr('string'),
  status: DS.attr('number'),
  desc: DS.attr('string'),
  category: DS.attr('string'),
  type: DS.attr('string'),
  item: DS.attr('string'),
  limit_price: DS.attr('number'),
  limit_weight: DS.attr('number'),
  kickoff_dt: DS.attr('string')
});

Groups.GroupController = Ember.ObjectController.extend({
  actions: {
    editGroup: function () {
      this.set('isEditing', true);
    },
    acceptChanges: function () {
      this.set('isEditing', false);

      if (Ember.isEmpty(this.get('model.title'))) {
        this.send('removeGroup');
      } else {
        this.get('model').save();
      }
    },
    removeGroup: function () {
      var group = this.get('model');
      group.deleteRecord();
      group.save();
    }
  },

  isEditing: false,

  isCompleted: function(key, value){
    var model = this.get('model');

    if (value === undefined) {
      // property being used as a getter
      var s = model.get('status');
      if ( s === 10 ){
        return false;
      }
      else {
        return true;
      }
    } else {
      var new_status = null;
      model.set('status', value ? 30:10);
      model.save();
      return value;
    }
  }.property('model.status')
});

Groups.GroupsController = Ember.ArrayController.extend({
  actions: {
    createGroup: function () {
      // Get the todo title set by the "New Todo" text field
      var title = this.get('newTitle');
      if (!title.trim()) { return; }

      // Create the new Todo model
      var group = this.store.createRecord('group', {
        title: title,
        status: 10
      });

      // Clear the "New Todo" text field
      this.set('newTitle', '');

      // Save the new model
      todo.save();
    },
    clearCompleted: function () {
      var completed = this.filterProperty('status', 30);
      completed.invoke('deleteRecord');
      completed.invoke('save');
    }
  },

  remaining: function () {
    return this.filterProperty('status', 10).get('length');
  }.property('@each.status'),

  inflection: function () {
    var remaining = this.get('remaining');
    return remaining === 1 ? 'item' : 'items';
  }.property('remaining'),

  hasCompleted: function () {
    return this.get('completed') > 0;
  }.property('completed'),

  completed: function () {
    return this.filterProperty('status', 30).get('length');
  }.property('@each.isCompleted'),
  
  allAreDone: function (key, value) {
    if (value === undefined) {
      return !!this.get('length') && this.everyProperty('isCompleted', 10);
    } else {
      this.setEach('isCompleted', value);
      this.invoke('save');
      return value;
    }
  }.property('@each.isCompleted')
});

Groups.EditTodoView = Ember.TextField.extend({
  didInsertElement: function () {
    this.$().focus();
  }
});

Ember.Handlebars.helper('edit-group', Groups.EditTodoView);