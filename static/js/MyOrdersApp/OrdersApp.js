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
						<h2><i className="halflings-icon user"></i><span className="break"></span>全部订单</h2>	
					</div>

					<div className="box-content">
						<div className="row-fluid">
									<div className="span2"><h3>订单编号</h3></div>
									<div className="span2"><h3>收货人</h3></div>
									<div className="span2"><h3>订单金额</h3></div>
									<div className="span2"><h3>订单时间</h3></div>
									<div className="span2"><h3>订单状态</h3></div>
									<div className="span2"><h3>操作</h3></div>
							</div>

							
								<div>{orderComps}</div>
							

					</div>


					
				</div>
			</div>

		)
	}
})
