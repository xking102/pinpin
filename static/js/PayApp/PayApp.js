var React = require('react');
var PayItems = require('./PayItems');


module.exports = React.createClass({
	getInitialState:function(){
		return {
			orders: []
		}
	},
	listOrders:function(){
		$.ajax({
            type:'get',
            url:'/api/v1/orders/'+ this.props.oid,
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
		var payComps = orders.map(function(item){
			return <PayItems key={item.id}
							order={item}  />

		});
		return (
			<div className="row-fluid">		
				<div>{payComps}</div>
			</div>

		)
	}
})
