var React = require('react');



module.exports = React.createClass({
	render:function(){
		return (
			<div>
				<div className="box-header" data-original-title>
					<h2>
						<i className="halflings-icon user"></i>
						<span className="break"></span>
							订单编号: {this.props.order.id}
					</h2>
				</div>

				<div className="box-content">
					<div className="row-fluid">
						<div className="span2 center"><h3></h3></div>
						<div className="span2 center"><h3>收货人</h3></div>
						<div className="span1 center"><h3>单价</h3></div>
						<div className="span1 center"><h3>数量</h3></div>
						<div className="span2 center"><h3>总价</h3></div>
						<div className="span2 center"><h3>实际价格</h3></div>
						<div className="span2 center"><h3>运费</h3></div>
					</div>

	                <div className="row-fluid">
	                    <div className="span2 center"><img src={this.props.order.image+".big.jpg"} /></div>
	                    <div className="span2 center">{this.props.order.create_userid}</div>
	                    <div className="span1 center">{this.props.order.unit_price}</div>
	                    <div className="span1 center">{this.props.order.req_qty}</div>
	                    <div className="span2 center">{this.props.order.total_price}</div>
	                    <div className="span2 center">{this.props.order.actual_price}</div>
	                    <div className="span2 center">{this.props.order.transfer_fee}</div>
	                </div>
	                
				</div>
			</div>
		)
	}
})
