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
			mans: order.mans
		};
	}
});


App.OrderController = Ember.ObjectController.extend({
	actions: {
		reqPlus: function () {
			if ( this.get('reqnum')  == this.get('model.amount') ) {

			}
			else {
				var price = this.get('model.price');
				var value = this.get('reqnum');
				this.set('reqnum',value + 1);
				var reqnum = this.get('reqnum');
				this.set('total',price*reqnum);
			}
		},
		reqMinus: function () {
			if ( this.get('reqnum') == 1) {

			}
			else {
				var price = this.get('model.price');
				var value = this.get('reqnum');
				this.set('reqnum',value - 1);
				var reqnum = this.get('reqnum');
				this.set('total',price*reqnum);
			}
			
		}
	},
	reqnum: function () {
		return 1
	}.property(),
	total: function(key){
    	var price = this.get('model.price');
    	var reqnum = this.get('reqnum');
    	console.log(this.get('model'));
		return reqnum*price;
  	}.property()
});


var order = {
	id: 1,
	title:'xxxxXXxxXXXXxxxxxXXXx',
	img: '/static/imgs/2.png',
	price: 15,
	amount: 30,
	mans: 12
};


