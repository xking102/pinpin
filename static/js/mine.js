App = Ember.Application.create();



App.Router.map(function() {
	this.resource('index', { path: '/' }, function() {
    	this.resource('groups');
    	this.resource('orders');
    	this.resource('products');
  	});
});


App.OrdersRoute = Ember.Route.extend({
	model: function() {
		return orders;
	}
});


App.ProductsRoute = Ember.Route.extend({
	model: function() {
		return products;
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


var products = [{
	id: 1,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 2,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 3,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 4,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 5,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 6,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 7,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 8,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 9,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 10,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
},
{
	id: 11,
	sku_id: 'JKD123',
	sku_img: '/static/imgs/2.png',
	title: 'dasfdf',
	desc: 'djkfsjdkl;fjaskdfj;klasdjfakdfj;;;;s;d;kfjasdf',
	create_user: 'XingKaixin',
	create_dt : '2015-01-01 22:22:22',
	isLike : true,
	like_dt : '2015-01-01 22:22:22',
	like_num: 5
}
];


var orders = [{
	id: 1,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '等待收货',
	isPay: true,
	isComplete: false
}, {
	id: 2,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '未付款',
	isPay: false,
	isComplete: false
}, {
	id: 3,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '已完成',
	isPay: true,
	isComplete: true
}, {
	id: 4,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '等待收货',
	isPay: true,
	isComplete: false
}, {
	id: 5,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '等待收货',
	isPay: true,
	isComplete: false
}, {
	id: 6,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '等待收货',
	isPay: true,
	isComplete: false
}, {
	id: 7,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '等待收货',
	isPay: true,
	isComplete: false
}, {
	id: 8,
	oid: 123456789,
	g_user:'Xingkaixin',
	sku_img: '/static/imgs/2.png',
	reciver: 'King',
	actual_price: 508.8,
	create_dt: '2015-01-01 22:22:22',
	status: '等待收货',
	isPay: true,
	isComplete: false
}

];