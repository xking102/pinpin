App = Ember.Application.create();


App.Router.map(function() {
	this.resource('index', { path: '/' }, function() {
    	this.resource('about');
    	this.resource('posts', function(){
    		this.resource('post',{path: ':post_id'});
    	});
  	});
});




App.PostsRoute = Ember.Route.extend({
	model: function() {
		 return posts;
	}
});


App.PostRoute = Ember.Route.extend({
	model: function(params) {
		 return posts.findBy('id', params.post_id);
	}
});



App.PostController = Ember.ObjectController.extend({
	isEditing: false,

	actions: {
		edit: function() {
			this.set('isEditing', true);
		},

		doneEditing: function() {
			this.set('isEditing', false);
		}
	}
});

Ember.Handlebars.helper('format-date', function(date) {
	moment.lang('zh-cn');
	return moment(date).fromNow();
});

var showdown  = new Showdown.converter();

Ember.Handlebars.helper('format-markdown', function(input) {
	return new Handlebars.SafeString(showdown.makeHtml(input));
});

var posts = [{
	id: '1',
	title: 'Rails is Omakase',
	author: {name: "d2h"},
	date: new Date('12-27-2012'),
	excerpt: "therskldjfa;df is djdfjaskdjfkl;asjdflk;asjdfkl;ajdkl;fajs;kdjfasdjfk;asdfjsad;f",
	body: "I want adjf Iwant I want I want I want I wnat iIwnte",
}, {
	id: '2',
	title: 'The Parley Letter',
	author: {name: "d2h"},
	date: new Date('12-24-2012'),
	excerpt: "Mydfasdf;skdjfk;asjkdfj asdjfkasdfdflk;asjdfkl;ajdkl;fajs;kdjfasdjfk;asdfjsad;f",
	body: "longlong sotrdfksajd;lkfjas;kldjfa;skldjflk;asjdfkl;asjdl;kfajs;dklfjaslk;djfal;ksjdf;laksjdf",
}];