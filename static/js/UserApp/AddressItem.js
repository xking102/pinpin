var React = require('react');
var mui = require('material-ui');
var {RaisedButton, FlatButton, Dialog, Paper} = mui;


module.exports = React.createClass({
    getInitialState:function(){
        return{
            modal:true,
            id:0,
            isDefault:false,
            address_line1:'',
            address_line2:'',
            tel:'',
            reciver:'',
            depth:5,
            setflag:false
        }
    },
    _MouseIn:function(){
      if(this.props.address.isDefault){

      }else{  
        var self = this
        if(this._timeout){
          clearTimeout(this._timeout);
        }
        this._timeout = setTimeout(function(){
          self.setState({
            setflag:true
          });
        },1000);
      }
    },
    _MouseOut:function(){
      var self = this
      if(this._timeout){
        clearTimeout(this._timeout);
      };
      this.setState({
        setflag:false
      });
    },
    handleDefault:function(){
      $.ajax({
          url      : '/api/v1/u/address/'+this.props.address.id,
          dataType : 'json',
          type     : 'put',
          contentType: "application/json",
          data:JSON.stringify({
                    'isDefault':true,
                    'address_line1':this.props.address.address_line1,
                    'address_line2':this.props.address.address_line2,
                    'tel':this.props.address.tel,
                    'reciver':this.props.address.reciver,
                  }),
          success: function(resp) {
            console.log('succ');
            this.setState({
              setflag:false
            })
            this.props.listAddress();
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
          }.bind(this)
        });
    },
    PutAddress:function(){
        $.ajax({
          url      : '/api/v1/u/address/'+this.state.id,
          dataType : 'json',
          type     : 'put',
          contentType: "application/json",
          data:JSON.stringify({
                    'isDefault':this.state.isDefault,
                    'address_line1':this.state.address_line1,
                    'address_line2':this.state.address_line2,
                    'tel':this.state.tel,
                    'reciver':this.state.reciver,
                  }),
          success: function(resp) {
            console.log('succ');
            this.props.listAddress();
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
          }.bind(this)
        });
    },
    DelAddress:function(){
        $.ajax({
          url      : '/api/v1/u/address/'+this.props.address.id,
          dataType : 'json',
          type     : 'delete',
          success: function(resp) {
            console.log('delete');
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
          }.bind(this)
        });
    },
    handleModify:function(){
        this.refs.customDialog.show();
        this.setState({
            id:this.props.address.id,
            isDefault:this.props.address.isDefault,
            tel:this.props.address.tel,
            reciver:this.props.address.reciver,
            address_line1:this.props.address.address_line1,
            address_line2:this.props.address.address_line2
        });
    },
    handleDelete:function(){
        this.DelAddress();
        this.props.listAddress();
    },
    _handleCustomDialogCancel:function(){
        this.refs.customDialog.dismiss();
    },
    _handleCustomDialogSubmit:function(){
        this.PutAddress();
        this.props.listAddress();
        this.refs.customDialog.dismiss();
    },
    _handlerReciver:function(e){
       this.setState({
            reciver:e.target.value
       })
    },
    _handlerTel:function(e){
       this.setState({
            tel:e.target.value
       })
    },
    _handlerAddress:function(e){
       this.setState({
            address_line1:e.target.value
       })
    },
    componentWillReceiveProps:function(nextProps) {
      console.log(nextProps);
    },
	render:function(){
        var customActions = [
        <FlatButton
            key={1}
            label="取消"
            labelStyle={{color:'rgb(170, 170, 170)'}}
            onTouchTap={this._handleCustomDialogCancel} />,
        <FlatButton
            key={2}
            label="修改"
            secondary={true}
            onTouchTap={this._handleCustomDialogSubmit} />
       ];
        var spandefault = {
            padding: '2px 5px',
            borderColor: '#ff3800',
            borderRadius: '3px',
            background: '#ffd6cc',
            color: '#f30',
            border: '1px solid #f60',
            textDecoration: 'none'
        }
	   var spantitle_style ={
            marginRight: '10px',
       };
       var tdtitle_style={
            verticalAlign: 'top',
            width: '100px',
       };
       var DefaultLink = this.props.address.isDefault?
       <div>
       <span style={spandefault}>默认地址</span></div>:
       <div/>;
       var setDefaultLink = this.state.setflag?
       <div>
       <span style={spandefault}>
        <a style={{color:'#f30'}} href="javascript:void(0)" onClick={this.handleDefault}>设为默认</a>
       </span>
       </div>:
       <div/>;
	   return (
            <div style={{marginBottom:'10px'}} className="row-fluid" onMouseEnter={this._MouseIn} onMouseLeave={this._MouseOut}>
        <Paper zDepth={this.state.depth}>
  <div className="span2">
            <p>address title {this.props.address.id}</p>
            <div>{DefaultLink}</div>
            <p><a href="javascript:void(0)" onClick={this.handleModify}>修改</a>/
            <a href="javascript:void(0)" onClick={this.handleDelete}>删除</a></p>
            <div>{setDefaultLink}</div>
            <div><Dialog
              ref="customDialog"
              title="修改收货地址"
              actions={customActions}
              modal={this.state.modal}>
               <label>收件人</label>
               <input  type="text" value={this.state.reciver} onChange={this._handlerReciver} />

               <label>联系电话</label>
               <input  type="text" value={this.state.tel} onChange={this._handlerTel} />

               <label>地址</label>
               <input  type="text" value={this.state.address_line1} onChange={this._handlerAddress} />


            </Dialog></div>
       </div>
      <div className="span8">
            <p>
                <span style={spantitle_style}>联系人</span>
                <span>{this.props.address.reciver}</span>
            </p>
            <p>
                <span style={spantitle_style}>电话</span>
                <span>{this.props.address.tel}</span>
            </p>
            <p>
                <span style={spantitle_style}>邮编</span>
                <span>0000</span>
            </p>
            <p>
                <span>{this.props.address.address_line1}</span>
            </p>
        </div>    
   </Paper>
</div>

		)
	}
})



