var React = require('react');


module.exports = React.createClass({
	getInitialState:function(){
		return {
			order: []
		}
	},
	listOrders:function(){
		$.ajax({
            type:'get',
            url:'/api/v1/orders/'+this.props.oid,
            datetype:'json'
        }).success(function (resp) {
        	console.log(resp);
        	this.setState({
            		order:resp.order
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
		return (
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2>
							<i className="halflings-icon user"></i>
							<span className="break"></span>
							订单编号:{this.props.oid}
						</h2>	
					</div>

					<div className="box-content">
						
						<div className="row-fluid">
								<div>￥ {this.state.order.total_price}</div>
								<div>放些有的没的~~~~</div>
						</div>
						

					
					</div>


					
				</div>
			</div>

		)
	}
})



