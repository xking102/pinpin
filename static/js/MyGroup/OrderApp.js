var React = require("react");

var OrderItem = require('./OrderItem')

var mui = require('material-ui');
var {Paper} = mui;


module.exports = React.createClass({
    
    render:function(){
        var orders = this.props.orders;
        var orderComps = orders.map(function(item){
            return <OrderItem key={item.id}
                            order={item}  />
        });
		return(
			<div>
                <div class="row-fluid">
                    <span className="span2">地址</span>
                    <span className="span1">收件人</span>
                    <span className="span1">电话</span>
                    <span className="span2">购买数量</span>
                    <span className="span5">总价</span>

                </div>
                <div class="row-fluid">
                    {orderComps}
                    <hr/>
                    
                </div>
                
            </div>

		)		
	}
})