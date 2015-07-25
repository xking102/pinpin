var React = require('react');
var mui = require('material-ui');
var {RaisedButton} = mui;

module.exports = React.createClass({
    getInitialState:function(){
        return{
            modal:false,
            id:0,
            isDefault:false,
            address_line1:'',
            address_line2:'',
            tel:'',
            reciver:''
        }
    },
    setDefault:function(){
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        $.ajaxSetup({
          beforeSend: function(xhr, settings) {
              if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
        }
        });
        $.ajax({
          url      : '/api/v1/u/address/'+this.props.id,
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
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
          }.bind(this)
        });
    },
    render:function(){
         console.log(this.props.address.id);
       var displayBtn = this.props.address.isDefault?
        <div key={this.props.id}>当前默认地址</div> :
        <RaisedButton key={this.props.id} label="设为默认"
            secondary={true}
            onTouchTap={this.setDefault} />;
        return (
            <div key={this.props.id}>
            {displayBtn}

</div>

        )
    }
})



