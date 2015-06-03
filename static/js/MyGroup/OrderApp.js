var React = require("react");

var OrderItem = req_qty('./OrderItem')

var mui = require('material-ui');
var {Paper} = mui;


module.exports = React.createClass({
    
    render:function(){
        var orders = this.props.orders;
        var orderComps = orders.map(function(item){
            return <OrderItem key={item.id}
                            order={item} 
                            saveOrder={this.props.saveOrder} />
        });
		return(
			<div>
                <div class="row-fluid">
                    <div class="span4">地址</div>
                    <div class="span1">收件人</div>
                    <div class="span2">电话</div>
                    <div class="span1">购买数量</div>
                    <div class="span1">总价</div>
                    <div class="span1">快递公司</div>
                    <div class="span1">快递单号</div>
                </div>
                <div class="row-fluid">
                    {orderComps}
                </div>
                
            </div>

		)		
	}
})