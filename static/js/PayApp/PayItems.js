var React = require('react');
var OrderItem = require('../OrderComponents/OrderItem');
var PayItem = require('./PayItem');



module.exports = React.createClass({
	render:function(){
		var order = this.props.order;
		return (
			<div className="row-fluid sortable">

				<div className="box span6">
					<OrderItem order={this.props.order} />
					
				</div>

				<div className="box span4">
					<PayItem order={this.props.order} />
					
				</div>

			</div>
		)
	}
})
