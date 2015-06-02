var React = require("react");


module.exports = React.createClass({
    
    render:function(){
        var status = this.props.group.status;
        var statusDesc;
        if (status==10){ 
            statusDesc = (
                <div>
                    <p>状态：拼团中</p>
                    <p>发布数量:{this.props.group.total_qty}</p>
                    <p>未付款数量:{this.props.group.req_qty}</p>
                    <p>已付款数量:{this.props.group.confirm_qty}</p>
                </div>
            );
        }else if(status==15){
            statusDesc = (
                <div>
                    <p>状态：拼团成功</p>
                    <p>需要购买数量:{this.props.group.total_qty}</p>
                </div>
            );
        }else if(status==20){
            statusDesc = (
                <div>
                    <p>状态：等待买家确认</p>
                    <p>发货数量:{this.props.group.total_qty}</p>
                    <p>未确认收货数量:{this.props.group.req_qty}</p>
                    <p>已确认收获数量:{this.props.group.confirm_qty}</p>
                </div>
            );
        }
        else if(status==30){
            statusDesc = (
                <div>
                    <p>状态：已完成</p>
                    <p>出售数量:{this.props.group.total_qty}</p>
                </div>
            );
        }
        else if(status==0){
            statusDesc = (
                <div>
                    <p>状态：取消</p>
                </div>
            );
        }else{
            statusDesc = (<div/>)
        }
		return (
			<div>
                {statusDesc}
            </div>

		)		
	}
})