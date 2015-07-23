var React = require('react');
var mui = require('material-ui');
var {RaisedButton, FlatButton, Dialog} = mui;

module.exports = React.createClass({
    getInitialState:function(){
        return{
            modal:true,
            id:0,
            isDefault:false,
            address_line1:'',
            address_line2:'',
            tel:'',
            reciver:''
        }
    },
    _clear:function(){
        this.setState({
            reciver:'',
            isDefault:false,
            address_line1:'',
            address_line2:'',
            tel:''

        })
    },
    _handleCustomDialogCancel:function(){
        this.refs.customDialog.dismiss();
        this._clear();
    },
    handleCustomDialogTouchTap:function() {
      this.refs.customDialog.show();
    },
    _handleCustomDialogSubmit:function(){
    var csrftoken = $('meta[name=csrf-token]').attr('content');
    console.log(csrftoken);
        $.ajaxSetup({
          beforeSend: function(xhr, settings) {
              if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
        }
    });
    $.ajax({
      url      : '/api/v1/u/address',
      dataType : 'json',
      type     : 'post',
      contentType: "application/json",
      data:JSON.stringify({
                'isDefault':this.state.isDefault,
                'address_line1':this.state.address_line1,
                'address_line2':this.state.address_line2,
                'tel':this.state.tel,
                'reciver':this.state.reciver,
              }),
      success: function(resp) {
        this.setState({
          id:resp.address.id,
          isDefault:resp.address.isDefault,
          tel:resp.address.tel,
          reciver:resp.address.reciver,
          address_line1:resp.address.address_line1,
          address_line2:resp.address.address_line2,
          create_dt:resp.address.create_dt,
          uid:resp.address.uid,
          update_dt:resp.address.update_dt
        });
        this.refs.customDialog.dismiss();
        var newAddress = {
            id:this.state.id,
            reciver:this.state.reciver,
            uid:this.state.uid,
            tel:this.state.tel,
            create_dt:this.state.create_dt,
            update_dt:this.state.update_dt,
            address_line1:this.state.address_line1,
            address_line2:this.state.address_line2,
            isDefault:this.state.isDefault
        };
        this.props.onNewAddress( newAddress );
        this._clear();
      }.bind(this),

      error: function(xhr, status, err) {
        console.error(status, err.toString);
      }.bind(this)
    });
  },
    handlerReciver:function(e){
      if(e.target.value.length<30){
        this.setState({
            reciver:e.target.value
       })
      }
    },
    handlerTel:function(e){
      if(e.target.value.length<30){
        this.setState({
            tel:e.target.value
       })
      }
    },
    handlerAddress:function(e){
      if(e.target.value.length<30){
        this.setState({
            address_line1:e.target.value
       })
      }
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
              title="新收货地址"
              actions={customActions}
              modal={this.state.modal}>
               <label>收件人</label>
               <input  type="text" value={this.state.reciver} onChange={this.handlerReciver} />

               <label>联系电话</label>
               <input  type="text" value={this.state.tel} onChange={this.handlerTel} />

               <label>地址</label>
               <input  type="text" value={this.state.address_line1} onChange={this.handlerAddress} />



            </Dialog>
            </div>

</div>

		)
	}

})



