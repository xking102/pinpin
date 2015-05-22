var React = require('react');



module.exports = React.createClass({
	render:function(){
		return (
			<div>
				<div className="box-header" data-original-title>
					<h2>
						<i className="halflings-icon user"></i>
						<span className="break"></span>
						订单: {this.props.order.id}
						</h2>	
				</div>

				<div className="box-content">
					<div className="row-fluid">
						订单的一些信息啊什么的就放这里
					</div>




				</div>
			</div>
		)
	}
})
