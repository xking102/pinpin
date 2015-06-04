var React = require("react");

var mui = require('material-ui');
var {Paper, TextField} = mui;


module.exports = React.createClass({
    getInitialState:function(){
        return {
            org:'',
            code:''
        }
    },
    saveOrder:function(){
        console.log('saveit',this.props.order.id);
        $.ajax({
          url      : '/api/v1/u/transport/'+this.props.order.id,
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
        console.log(this.props);
		return(
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

		)		
	}
})