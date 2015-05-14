App = Ember.Application.create();



App.Router.map(function() {
	this.resource('order', { path: '/' });
});


App.OrderRoute = Ember.Route.extend({
	model: function() {
		return {
			id: order.id,
			title: order.title,
			img: order.img,
			price: order.price,
			amount: order.amount,
			reqnum: 1,
			mans: order.mans
		};
	}
});


App.OrderController = Ember.ObjectController.extend({
	actions: {
		reqPlus: function () {
			var value = this.get('model.reqnum');
			console.log(value);
		},
		reqMinus: function () {

		}
	},
	total: function(key){
    	var price = this.get('model.price');
    	var reqnum = this.get('model.reqnum');
		return reqnum*price;
  	}.property('model.price')
});


var order = {
	id: 1,
	title:'xxxxXXxxXXXXxxxxxXXXx',
	img: '/static/imgs/2.png',
	price: 15,
	amount: 30,
	mans: 12
};


