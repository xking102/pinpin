var React = require("react");

var mui = require('material-ui');
var {Paper, TextField, Checkbox} = mui;


module.exports = React.createClass({
    propTypes: {
        viewMode: React.PropTypes.string
    },
    getDefaultProps: function() {
        return {
          viewMode:'Transport'
        }
    },
    getInitialState:function(){
        return {
            org:'',
            code:''
        }
    },
    saveOrder:function(){
        var csrftoken = $('meta[name=csrf-token]').attr('content');
        $.ajaxSetup({
          beforeSend: function(xhr, settings) {
              if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                  xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
        }
        });
        console.log('saveit',this.props.order.id);
        $.ajax({
          url      : '/order_pre_send/'+this.props.order.id,
          dataType : 'json',
          type     : 'put',
          contentType: "application/json",
          data:JSON.stringify({
                    'transcode':this.state.code,
                    'transorg':this.state.org
                  }),
          success: function(resp) {
            console.log('succ');
          }.bind(this),
          error: function(xhr, status, err) {
            console.error(status, err.toString);
          }.bind(this)
        });
    },
    handleBlurTransportOrg:function(){
        console.log('dialog-orderid',this.props.order.id);
        console.log('dialog-ordersave');
        this.saveOrder();
    },
    handlerTransportOrg:function(e){
        this.setState({
            org:e.target.value
        });
    },
    handleBlurTransportCode:function(){
        console.log('dialog-orderid',this.props.order.id);
        console.log('dialog-ordersave');
        this.saveOrder();
    },
    handlerTransportCode:function(e){
        this.setState({
            code:e.target.value
        });
    },
    componentDidMount:function(){
        this.setState({
            org:this.props.order.transport.transorg,
            code:this.props.order.transport.transcode
        });
    },
    render:function(){
        var isConfirm = false;
        if(this.props.order.status==35){
            isConfirm=true;
        }else{this.props.order.status==30}{
            isConfirm=false;
        }
        var Transport = (
            <div>
             <span className="span2">1{this.props.order.transport.address_line1}</span>
             <span className="span1">2{this.props.order.transport.reciver}</span>
             <span className="span1">3{this.props.order.transport.tel}</span>
             <span className="span2">4{this.props.order.req_qty}</span>
             <span className="span1">5{this.props.order.total_price}</span>
             <span className="span2">
                 <TextField style={{width:'97px'}}
                     hintText="输入快递公司"
                     type='text'
                     value={this.state.org}
                     onBlur={this.handleBlurTransportOrg}
                     onChange={this.handlerTransportOrg}
                 />
             </span>
             <span className="span3">
                 <TextField style={{width:'97px'}}
                     hintText="输入快递单号"
                     type='text'
                     value={this.state.code}
                     onBlur={this.handleBlurTransportCode}
                     onChange={this.handlerTransportCode}
                 />
             </span>
            </div>
        );
        var Pay = (
            <div>
            <span className="span2">1{this.props.order.transport.address_line1}</span>
            <span className="span1">2{this.props.order.transport.reciver}</span>
            <span className="span1">3{this.props.order.transport.tel}</span>
            <span className="span2">4{this.props.order.req_qty}</span>
            <span className="span1">5{this.props.order.total_price}</span>
            <span className="span1">6{this.props.order.transport.code}</span>
            <span className="span1">7{this.props.order.transport.org}</span>
            <span className="span1">
                <Checkbox
                    name="PayConfirmBox"
                    value="isConfirm"
                    defaultChecked={isConfirm}
                    disabled={true}
                />
            </span>
            </div>
        );
        var viewMode = (<div/>);
        if(this.props.viewMode='Transport'){
            viewMode = Transport;
        }else if(this.props.viewMode='Pay'){
            viewMode = Pay;
        }else{

        }
		return(
			<div>
                {viewMode}
            </div>

		)
	}
})
