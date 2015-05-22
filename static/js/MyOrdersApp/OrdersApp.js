var React = require('react');
var OrderItem = require('./OrderItem');


module.exports = React.createClass({
	getInitialState:function(){
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
							order={item}  />
		});
		return (
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2><i className="halflings-icon user"></i><span className="break"></span>Orders</h2>	
					</div>

					<div className="box-content">
						<div className="row-fluid">
									<div className="span3"><h3>id</h3></div>
									<div className="span3"><h3>title</h3></div>
									<div className="span3"><h3>price</h3></div>
									<div className="span3"><h3>Actions</h3></div>
							</div>

							
								<div>{orderComps}</div>
							

					</div>


					
				</div>
			</div>

		)
	}
})
