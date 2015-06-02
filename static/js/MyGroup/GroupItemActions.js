var React = require("react");
var mui = require('material-ui');
var {RaisedButton} = mui;

module.exports = React.createClass({
    _handleCancel:function(){
        alert('cancel');
    },
    _handleDeliver:function(){
        alert('deliver');
    },
    _handleViewOrder:function(){
        alert('viewOrder');
        /*
        status==15
        status==20
        多列出确认状态
        */
    },
    render:function(){
        var status = this.props.group.status;
        var req_qty = this.props.group.req_qty;
        var confirm_qty = this.props.group.confirm_qty;
        var actionBtn;
        if (status==10&&req_qty==0&&confirm_qty==0){
            return 
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
		return(
			<div>
                {actionBtn}
            </div>

		)		
	}
})