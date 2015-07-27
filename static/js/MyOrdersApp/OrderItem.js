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
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        $.ajaxSetup({
          beforeSend: function(xhr, settings) {
              if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
        }
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
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        $.ajaxSetup({
          beforeSend: function(xhr, settings) {
              if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
        }
        });
        $.ajax({
            type:'put',
            url:'/order_confirm/'+this.props.order.id,
            contentType: "application/json",
            success:function (resp) {
                 this.setState(
                    {query_flag: true}
                );
                 // this.props.changeOrderStatus(this.props.order.id,35)
                 window.location.href = resp.url;
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
        var displayBtn = '';
        var transorg ='';
        var transcode = '';
        switch(status)
        {
            case 1:
            statusName = '草稿';
            break
            case 0:
            statusName = '订单取消'
            break
            case 10:
            statusName = '待确认'
            displayBtn =
            <div><a className="btn btn-link" href={"order#/"+this.props.order.id+"/pay"}>确认订单信息</a><br></br>
            <a className="btn btn-link" href="javascript:void(0)" onClick={this.handlerCancel}>取消订单</a></div>
            break
            case 20:
            statusName = '待付款'
            displayBtn =
            <div><a className="btn btn-link" href={"order#/"+this.props.order.id+"/pay"}>支付</a><br></br>
            <a className="btn btn-link" href="javascript:void(0)" onClick={this.handlerCancel}>取消订单</a></div>
            break
            case 25:
            statusName = '等待团长发货'
            //displayBtn = <a className="btn btn-link" href={"order#/"+this.props.order.id+"/complain"}>投诉</a>
            break
            case 30:
            statusName = '等待收货'
            transorg= '快递公司:'+this.props.order.transport.transorg
            transcode= '运单号:'+this.props.order.transport.transcode
            displayBtn = <div><a className="btn btn-link" href="javascript:void(0)" onClick={this.handlerConfirm}>确认收货</a><br></br></div>
            break
            case 35:
            statusName = '完成'
            break
        }
		return(

			<div style={{marginBottom:'15px'}} onMouseEnter={this.MouseIn} onMouseLeave={this.MouseOut}>
                <div className="row-fluid"><h5>{this.props.order.trade_no}</h5></div>
                <div className="row-fluid">
                    <div className="span2 center"><img src={this.props.order.image+".big.jpg"} /></div>
                    <div className="span2 center">{this.props.order.create_userid}</div>
                    <div className="span2 center">
                    {this.props.order.total_price}
                    </div>
                    <div className="span2 center">{this.props.order.create_dt}</div>
                    <div className="span2 center">
                    <p>{statusName}</p>
                    <p>{transorg}</p>
                    <p>{transcode}</p></div>
                    <div className="span2 center">
                        {displayBtn}
                    </div>
                </div>
            </div>

		)
	}
})
