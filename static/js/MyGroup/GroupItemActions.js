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
            modal:false
            orders:[]
        }
    },
    _handleCancel:function(){
        alert('cancel');
    },
    _handleDeliver:function(){
        alert('deliver');
        this.deliverGroup();
    },
    _handleViewOrder:function(){
        // this.context.router.transitionTo('detail', {gid: this.props.group.id});
        listGroupOrders();
        console.log(this.state.orders);
        this.refs.viewOrder.show();
        /*
        status==15
        status==20
        多列出确认状态
        */
    },
    _handlecustomAddressClose:function(){
        this.refs.viewOrder.dismiss();
    },
    saveOrder:function(oid){
        console.log('saveit',oid);
    },
    deliverGroup:function(){
        //requtest the group to delivery
    }
    listGroupOrders:function(){
        $.ajax({
            type:'get',
            url:'/u/group/'+ this.props.group.id,
            datetype:'json',
            success:function (resp) {
                this.setState({
                        orders:resp.orders
                    });
            }.bind(this),
            error:function(){
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
                        onTouchTap={this._handleViewOrder} 
                    />
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
                        onTouchTap={this._handleViewOrder} 
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
        var viewOrder = [
        <FlatButton
            key={1}
            label="关闭"
            labelStyle={{color:'rgb(170, 170, 170)'}}
            onTouchTap={this._handlecustomAddressClose} />
        ];
		return(
			<div>
            <Dialog
              ref="viewOrder"
              title="拼团用户信息"
              actions={viewOrder}
              modal={this.state.modal}>
               <OrderApp order={this.state.orders}
                        saveOrder={this.saveOrder} />
               
            </Dialog>
                {actionBtn}
            </div>

		)		
	}
})