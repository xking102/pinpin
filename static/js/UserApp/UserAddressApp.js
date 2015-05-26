var React = require('react');
var mui = require('material-ui');
var {RaisedButton, FlatButton, Dialog} = mui;

module.exports = React.createClass({
    getInitialState:function(){
        return{
            modal:false
        }
    },
	_handleCustomDialogSubmit:function(){
        this.refs.customDialog.dismiss();
    },
    _handleCustomDialogCancel:function(){
        this.refs.customDialog.dismiss();
    },
    handleCustomDialogTouchTap:function() {
      this.refs.customDialog.show();
    },

	render:function(){
	   var spantitle_style ={
            margiRight: '10px',
       };
       var tdtitle_style={
            verticalAlign: 'top',
            width: '100px',
       };
       var customActions = [
        <FlatButton
            key={1}
            label="取消"
            labelStyle={{color:'rgb(170, 170, 170)'}}
            onTouchTap={this._handleCustomDialogCancel} />,
        <FlatButton
            key={2}
            label="添加"
            secondary={true}
            onTouchTap={this._handleCustomDialogSubmit} />
       ];
		return (
            <div>
            <div style={{marginBottom:'40px',marginLeft:'20px'}}>
            <RaisedButton label="添加一个新地址" 
            secondary={true}
            onTouchTap={this.handleCustomDialogTouchTap} />
            <Dialog
              ref="customDialog"
              title="Dialog With Custom Actions"
              actions={customActions}
              modal={this.state.modal}>
              就在这里加
            </Dialog>
            </div>
			<table style={{marginLeft: '30px'}}>
    <tr>
        <td style={tdtitle_style}>
            address title
        </td>

        <td style={{width: '50px'}}>
           
        </td>
        
        <td>
            <p>
                <span style={spantitle_style}>联系人</span>
                <span>1111111</span>
            </p>
            <p>
                <span style={spantitle_style}>电话</span>
                <span>1111111</span>
            </p>
            <p>
                <span style={spantitle_style}>邮编</span>
                <span>1111111</span>
            </p>
            <p>
                <span>xx国xx市xx区xx路xx号xx楼xx室</span>
            </p>
            
        </td>
    </tr>
</table>
</div>

		)
	}
})



