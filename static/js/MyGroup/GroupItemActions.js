var React = require("react");
var mui = require('material-ui');
var {RaisedButton, FlatButton, Dialog} = mui;

var OrderApp = require('./OrderApp');

module.exports = React.createClass({
    contextTypes: {
        router: React.PropTypes.func.isRequired
    },
    getInitialState:function(){
        return {
            modal:true,
            orders:[]
        }
    },
    _handleCancel:function(){
        console.log('cancel');
        $.ajax({
          url      : '/u/group/'+this.props.group.id+'/cancel',
          dataType : 'json',
          type     : 'put',
          contentType: "application/json",
          success: function(resp) {
            console.log('succ');
            this.props.changeGroupStatus(this.props.group.id,0);
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
          }.bind(this)
        });
    },
    _handleDeliver:function(){
        console.log('deliver');
        this.deliverGroup();
    },
    _handleOrderPay:function(){
        this.listGroupOrders();
        console.log('handleOrderPay')
        this.refs.viewOrderPay.show();
    },
    _handleOrderTransport:function(){
        // this.context.router.transitionTo('detail', {gid: this.props.group.id});
        this.listGroupOrders();
        this.refs.viewOrderTransport.show();
        /*
        status==15
        status==20
        多列出确认状态
        */
    },
    _handlecustomAddressClose:function(){
        this.refs.viewOrderTransport.dismiss();
    },
    _handlecustomPayClose:function(){
        this.refs.viewOrderPay.dismiss();
    },
    deliverGroup:function(){
        $.ajax({
          url      : '/u/group/'+this.props.group.id+'/delivery',
          dataType : 'json',
          type     : 'put',
          contentType: "application/json",
          success: function(resp) {
            status = resp.status;
            if(status=='succ'){
                console.log('succ');
                this.props.changeGroupStatus(this.props.group.id,20);
                console.log('renew~')
            }else{
                console.log('fail');
            }
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
          }.bind(this)
        });
    },
    listGroupOrders:function(){
        $.ajax({
            type:'get',
            url:'/u/group/' + this.props.group.id,
            success:function (resp) {
                this.setState({
                    orders:resp.orders
                });
            }.bind(this),
            error:function(xhr, status, err){
                console.error(status, err.toString);
            }.bind(this)
        });
    },
    render:function(){
        var status = this.props.group.status;
        var req_qty = this.props.group.req_qty;
        var confirm_qty = this.props.group.confirm_qty;
        var actionBtn;
        if (status==10&&req_qty==0&&confirm_qty==0){ 
            actionBtn = (
                <div>
                    <RaisedButton label="取消" 
                        secondary={true}
                        onTouchTap={this._handleCancel} 
                    />
                </div>
            );
        }else if(status==10){
            actionBtn = (
                <div>
                  
                </div>
            );
        }else if(status==15){
            actionBtn = (
                <div>
                    <RaisedButton label="查看团员信息" 
                        secondary={true}
                        onTouchTap={this._handleOrderTransport} 
                    />
                    &nbsp;
                    <RaisedButton label="发货" 
                        secondary={true}
                        onTouchTap={this._handleDeliver} 
                    />
                </div>
            );
        }else if(status==20){
            actionBtn = (
                <div>
                    <RaisedButton label="查看确认订单详情" 
                        secondary={true}
                        onTouchTap={this._handleOrderPay} 
                    />
                </div>
            );
        }
        else if(status==30){
            actionBtn = (
                <div>
                  
                </div>
            );
        }
        else if(status==0){
            actionBtn = (
                <div>
                  
                </div>
            );
        }
        else{
            actionBtn = (<div/>)
        }
        var viewOrderTransport = [
        <FlatButton
            key={1}
            label="关闭"
            labelStyle={{color:'rgb(170, 170, 170)'}}
            onTouchTap={this._handlecustomAddressClose} />
        ];
        var viewOrderPay = [
        <FlatButton
            key={1}
            label="关闭"
            labelStyle={{color:'rgb(170, 170, 170)'}}
            onTouchTap={this._handlecustomPayClose} />
        ];
		return(
			<div>
            <Dialog
              ref="viewOrderTransport"
              title="拼团用户信息"
              actions={viewOrderTransport}
              modal={this.state.modal}>
               <OrderApp orders={this.state.orders} viewMode={'Transport'}/>
               
            </Dialog>
            <Dialog
              ref="viewOrderPay"
              title="订单确认状况"
              actions={viewOrderPay}
              modal={this.state.modal}>
               <OrderApp orders={this.state.orders} viewMode={'Pay'} />
               
            </Dialog>
                {actionBtn}
            </div>

		)		
	}
})