var React = require('react');
var mui = require('material-ui');
var {TextField, RaisedButton, Snackbar} = mui

module.exports = React.createClass({
	getInitialState:function(){
        return{
            query:false,
            errorText:'',
            old_pw:'',
            new_pw:'',
            confirm_pw:'',
            message:''
        }
    },
	handlerOldPassword:function(e){
		this.setState({
			old_pw:e.target.value
		});
	},
	handlerNewPassword:function(e){
		this.setState({
			new_pw:e.target.value
		});
	},
	handlerConfirmPassword:function(e){
		this.setState({
			confirm_pw:e.target.value
		});
	},
	handleBlurPW:function(){
		if(this.state.new_pw==this.state.confirm_pw){
			this.setState({
				query:true,
				errorText:''
			})
		}else{
			this.setState({
				query:false,
				errorText:'两次密码输入不一致'
			})
		}

	},
	handleModify:function(){
		if(this.state.query){
			this.changePWJSON();
		}
		else{
			return
		}
	},
	changePWJSON:function(){
    var csrftoken = $('meta[name=csrf-token]').attr('content');
    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
    }
    });
    $.ajax({
      url      : '/password',
      dataType : 'json',
      type     : 'put',
      contentType: "application/json",
      data:JSON.stringify({
                'old_password':this.state.old_pw,
                'new_password':this.state.new_pw
              }),
      success: function(resp) {
        this.setState({
          message:resp.messages
        });
        this.refs.snackbar.show();
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(status, err.toString);
      }.bind(this)
    });
  },
	render:function(){
		return (
			<div style={{marginTop:'10px',marginLeft:'40%'}} className="row-fluid">

				<TextField
  					hintText="请输密码"
  					type='password'
  					floatingLabelText="在这输入旧密码"
  					onChange={this.handlerOldPassword}
  				/>
  				<br/>
  				<TextField
  					hintText="请输新密码"
  					type='password'
  					errorText={this.state.errorText}
  					floatingLabelText="在这输入新密码"
  					onBlur={this.handleBlurPW}
  					onChange={this.handlerNewPassword}
  				/>
  				<br/>
  				<TextField
  					hintText="重复一遍新密码"
  					type='password'
  					errorText={this.state.errorText}
  					floatingLabelText="重新输一遍"
  					onBlur={this.handleBlurPW}
  					onChange={this.handlerConfirmPassword}
  				/>
  				<br/>
  				<RaisedButton style={{marginBottom:'40px',marginTop:'20px'}}  label="确认修改"
            		secondary={true}
            		onTouchTap={this.handleModify} />
            	<br/>
            	<Snackbar
          			ref="snackbar"
          			message={this.state.message}
          		/>
			</div>

		)
	}
})



