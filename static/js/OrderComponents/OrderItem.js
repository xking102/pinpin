var React = require('react');



module.exports = React.createClass({
	render:function(){
		var order = this.props.order;
		return (
			<div>
				{order.id}
				
			</div>

		)
	}
})
