var React = require("react");

var mui = require('material-ui');
var {Paper} = mui;


module.exports = React.createClass({
    getInitialState:function(){
        return {
            org:'',
            code:''
        }
    },
    handleBlurTransportOrg:function(){
        console.log('dialog-orderid',this.props.order.id);
        console.log('dialog-ordersave');
        this.props.saveOrder(this.props.order.id);
    },
    handlerTransportOrg:function(e){
        this.setState({
            org:e.target.value
        });
    },
    handleBlurTransportCode:function(){
        console.log('dialog-orderid',this.props.order.id);
        console.log('dialog-ordersave');
        this.props.saveOrder(this.props.order.id);
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
		return(
			<div>
                <div class="span4">{this.props.order.transport.address_line1}</div>
                <div class="span1">{this.props.order.transport.reciver}</div>
                <div class="span2">{this.props.order.transport.tel}</div>
                <div class="span1">{this.props.order.req_qty}</div>
                <div class="span1">{this.props.order.total_price}</div>
                <div class="span1">
                    <TextField
                        hintText="输入快递公司"
                        type='text'
                        value={this.state.org}
                        onBlur={this.handleBlurTransportOrg}
                        onChange={this.handlerTransportOrg} 
                    />
                </div>
                <div class="span1">
                    <TextField
                        hintText="输入快递单号"
                        type='text'
                        value={this.state.code}
                        onBlur={this.handleBlurTransportCode}
                        onChange={this.handlerTransportCode} 
                    />
                </div>
            </div>

		)		
	}
})