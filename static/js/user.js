App = Ember.Application.create();



App.Router.map(function() {
	this.resource('index', { path: '/' }, function() {
    	this.resource('info');
    	this.resource('addresses');
    	this.resource('password');
  	});
});


App.InfoRoute = Ember.Route.extend({
	model: function() {
		return info;
	}
});

App.AddressesRoute = Ember.Route.extend({
	model: function() {
		return addresses;
	}
});




Ember.Handlebars.helper('format-date', function(date) {
	return moment(date).format('YYYY-MM-DD');
});

Ember.Handlebars.helper('format-time', function(date) {
	return moment(date).format('HH:mm:ss');
});


Ember.Handlebars.helper('format-fromnow', function(date) {
	return moment(date).fromNow();
});



var info = [{
	id: 1,
	nickname:'Kevin',
	user_img: '/static/imgs/3.jpg',
	email: 'kevin@pinpin.com',
	reg_dt: '2015-01-01 22:22:22'
}
];



var addresses = [{
	id: 1,
	address_line1: 'shanghai,china',
	address_line2: 'Road.123 No.123',
	isDefault: false
}, {
	id: 2,
	address_line1: 'shanghai,china',
	address_line2: 'Road.456 No.456',
	isDefault: true
}, {
	id: 3,
	address_line1: 'shanghai,china',
	address_line2: 'Road.789 No.789',
	is_default: false
}, {
	id: 4,
	address_line1: 'shanghai,china',
	address_line2: 'Road.xxx No.xxx',
	isDefault: false
}
];