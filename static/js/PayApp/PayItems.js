var React = require('react');
var OrderItem = require('../OrderComponents/OrderItem');
var PayItem = require('./PayItem');



module.exports = React.createClass({
	render:function(){
		var order = this.props.order;
		return (
			<div>
				<div>

					<OrderItem order={order} />
				</div>

				<div>
					<PayItem />
				</div>
			</div>	
		)
	}
})
