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
			if ( this.get('model.reqnum')  == this.get('model.amount') ) {

			}
			else {
				var model = this.get('model');
				var price = this.get('model.price');
				var value = this.get('model.reqnum');
				this.set('model.reqnum',value + 1);
				var reqnum = this.get('model.reqnum');
				this.set('total',price*reqnum);
			}
		},
		reqMinus: function () {
			if ( this.get('model.reqnum') == 1) {

			}
			else {
				var model = this.get('model');
				var price = this.get('model.price');
				var value = this.get('model.reqnum');
				this.set('model.reqnum',value - 1);
				var reqnum = this.get('model.reqnum');
				this.set('total',price*reqnum);
			}
			
		}
	},
	total: function(key){
    	var price = this.get('model.price');
    	var reqnum = this.get('model.reqnum');
    	console.log(this.get('model'));
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


