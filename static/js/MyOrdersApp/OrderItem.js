var React = require("react");
var mui = require('material-ui');
var {Paper} = mui;

module.exports = React.createClass({

    contextTypes: {
        router: React.PropTypes.func.isRequired
    },
    
    getInitialState:function(){
        return {
            query_flag: false,
            depth:3
        }
    },
    MouseIn:function(){
        this.setState({
            depth:1
        });
    },
    MouseOut:function(){
        this.setState({
            depth:3
        });
    },
    handlerCancel: function(){
        if(this.state.query_flag){
            console.log('waiting');
        }else{
        this.setState({
            query_flag: true
        });
        $.ajax({
            type:'put',
            url:'/order_cancel/'+this.props.order.id,
            contentType: "application/json",
            success:function (resp) {
                 this.setState(
                    {query_flag: true}
                );
                 this.props.changeOrderStatus(this.props.order.id,0)
            }.bind(this),
            error:function (resp){
                                 this.setState(
                    {query_flag: false}
                );
            }.bind(this)

        });             
    }
    },
    handlerConfirm: function(){
        if(this.state.query_flag){
            console.log('waiting');
        }else{
        this.setState({
            query_flag: true
        });
        $.ajax({
            type:'put',
            url:'/order_confirm/'+this.props.order.id,
            contentType: "application/json",
            success:function (resp) {
                 this.setState(
                    {query_flag: true}
                );
                 this.props.changeOrderStatus(this.props.order.id,35)
            }.bind(this),
            error:function (resp){
                                 this.setState(
                    {query_flag: false}
                );
            }.bind(this)

        });             
    }
    },
    render:function(){
        var status = this.props.order.status;
        var statusName ='未知状态';
        var displayBtn = ''
        var mod = this.props.order.id%3;
        var stylecolor = "greenDark";
        if(mod == 0){
            stylecolor = "greenLight";
        }else if(mod == 1){
            stylecolor = "green";
        }else{
            stylecolor = "greenLight";
        };
        stylecolor = "circleStatsItemBox " + stylecolor;
        switch(status)
        {
            case 1:
            statusName = '草稿';
            break
            case 0:
            statusName = '订单取消'
            break
            case 10:
            statusName = '订单申请中'
            break
            case 20:
            statusName = '待付款'
            displayBtn = 
            <div><a className="btn btn-link" href={"order#/"+this.props.order.id+"/pay"}>支付</a><br></br>
            <a className="btn btn-link" href="javascript:void(0)" onClick={this.handlerCancel}>取消订单</a></div>
            break
            case 25:
            statusName = '待发货'
            displayBtn = <a className="btn btn-link" href={"order#/"+this.props.order.id+"/complain"}>投诉</a>
            break
            case 30:
            statusName = '待收货'
            displayBtn = <div><a className="btn btn-link" href="javascript:void(0)" onClick={this.handlerConfirm}>确认收货</a><br></br>
            <a className="btn btn-link" href={"order#/"+this.props.order.id+"/complain"}>投诉</a></div>
            break
            case 35:
            statusName = '完成'
            break
        }
		return(

			<div style={{marginBottom:'15px'}} onMouseEnter={this.MouseIn} onMouseLeave={this.MouseOut}>
                <div className="row-fluid">{this.props.order.id}</div>
                <div className="row-fluid">
                    
                    <div className="span2 center"><img alt="香水" src="/static/imgs/orders/OrderItems.png"/></div>
                    <div className="span2 center">{this.props.order.create_userid}</div>
                    <div className="span2 center">
                    <p>{this.props.order.total_price}</p>
                    <p>在线支付</p>
                    </div>
                    <div className="span2 center">{this.props.order.create_dt}</div>
                    <div className="span2 center">{statusName}</div>
                    <div className="span2 center">
                        <a className="btn btn-link" href={"order#/"+this.props.order.id}>
                            查看
                        </a><br></br>
                        {displayBtn}
                    </div>
                </div>
            </div>

		)		
	}
})