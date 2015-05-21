var React = require('react');
var OrderItem = require('./OrderItem');


module.exports = React.createClass({
	getInitialState:function(){
		var orders = [
			{
				id: 1,
				title:'订单1',
				price: 137
			},
			{
				id: 2,
				title:'订单2',
				price: 137
			},
			{
				id: 3,
				title:'订单3',
				price: 137
			},
			{
				id: 4,
				title:'订单4',
				price: 137
			},
			{
				id: 5,
				title:'订单5',
				price: 137
			},
			{
				id: 6,
				title:'订单6',
				price: 137
			},
			{
				id: 7,
				title:'订单7',
				price: 137
			},
			{
				id: 8,
				title:'订单8',
				price: 137
			},
			{
				id: 9,
				title:'订单9',
				price: 137
			}
			
		];
		return {
			orders: []
		}
	},
	listOrders:function(){
		$.ajax({
            type:'get',
            url:'/api/v1/u/orders',
            datetype:'json'
        }).done(function (resp) {
        	this.setState({
            		orders:resp.orders
            	});
            console.log(this.state.orders);
        }.bind(this));
	},
	componentDidMount : function(){
		this.listOrders();
	},
	componentWillReceiveProps  : function(){
		this.listOrders();
	},
	render:function(){
		var orders = this.state.orders;
		var orderComps = orders.map(function(item){
			return <OrderItem key={item.id}
							id={item.id} 
							gid={item.gid}
							price={item.unit_price} />

		});
		return (
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2><i className="halflings-icon user"></i><span className="break"></span>Orders</h2>	
					</div>

					<div className="box-content">
						<div className="row-fluid">
									<div className="span3">id</div>
									<div className="span3">title</div>
									<div className="span3">price</div>
									<div className="span3">Actions</div>
								
							</div>

							
								<div>{orderComps}</div>
							

					</div>


					
				</div>
			</div>

		)
	}
})
