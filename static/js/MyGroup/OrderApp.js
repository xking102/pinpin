var React = require("react");

var OrderItem = require('./OrderItem')

var mui = require('material-ui');
var {Paper} = mui;


module.exports = React.createClass({
    propTypes: {
        viewMode: React.PropTypes.string
    },
    getDefaultProps: function() {
        return {
          viewMode:'Transport'
        }
    },
    render:function(){
        var Transport = (
            <div>
            <span className="span2">地址</span>
            <span className="span1">收件人</span>
            <span className="span1">电话</span>
            <span className="span2">购买数量</span>
            <span className="span5">总价</span>
            </div>
        );
        var Pay = (
            <div>
            <span className="span2">地址</span>
            <span className="span1">收件人</span>
            <span className="span1">电话</span>
            <span className="span2">购买数量</span>
            <span className="span1">总价</span>
            <span className="span1">运单号</span>
            <span className="span1">运单公司</span>
            <span className="span1">已确认</span>
            </div>
        );
        var orders = this.props.orders;
        var orderComps = orders.map(function(item){
            return <OrderItem key={item.id}
                            order={item} viewMode={this.props.viewMode} />
        }.bind(this));
        var viewMode = (<div/>);
        if(this.props.viewMod=='Transport'){
            viewMode = Transport;
        }else if(this.props.viewMod=='Pay'){
            viewMode = Pay;
        }
        else{
            
        }
		return(
			<div>
                <div class="row-fluid">
                    {viewMode}

                </div>
                <div class="row-fluid">
                    {orderComps}
                    <hr/>
                    
                </div>
                
            </div>

		)		
	}
})