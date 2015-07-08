var React = require('react');
var OrderItem = require('../OrderComponents/OrderItem');
var AddressItem = require('./AddressItem');



module.exports = React.createClass({
	getInitialState:function(){
		return {
			address: [],
			CurrentAddressId:''
		}
	},
	listAdress:function(){
	    $.ajax({
	      url      : '/api/v1/u/address',
	      dataType : 'json',
	      type     : 'GET',
	      success: function(resp) {
	        this.setState({
	          address:resp.addresses
	        });
	      }.bind(this),
	      error: function(resp) {
	        console.log("出错了");
	      }.bind(this)
	    });
	  },
	setCurrentAddress:function(id){
		this.setState(
            {CurrentAddressId:id}
         );
	  },
	setTransAdress:function(){
	    $.ajax({
	      url      : '/api/v1/u/transport',
          contentType: "application/json",
	      type     : 'POST',
	      data:JSON.stringify({
              'oid':this.props.order.id,
              'aid':this.state.CurrentAddressId
           }),
	      success: function(resp) {
	        console.log("OK");
	      }.bind(this),
	      error: function(resp) {
	        console.log("出错了");
	      }.bind(this)
	    });
	},
	componentDidMount : function(){
		this.listAdress();
	},
	componentWillReceiveProps  : function(){
		this.listAdress();
	},
	render:function(){
		var order = this.props.order;
		var address = this.state.address;
		var Myaddress = address.map(function(item){
			return <AddressItem key={item.id}
							addr={item} setCurrentAddress={this.setCurrentAddress} />
		}.bind(this));

		return (
			<div className="row-fluid sortable">

				<div className="box span12">
					<OrderItem order={this.props.order}/>
					
				</div>

				<div className="box span12">

				        <div className="box-header" data-original-title>
          <h2>
            <i className="halflings-icon user"></i>
            <span className="break"></span>
            收货人信息：
            </h2> 
        </div>

              <div className="row-fluid">
                  <div className="span2"><h3>收货人</h3></div>
                  <div className="span6"><h3>地址</h3></div>
                  <div className="span2"><h3>电话</h3></div>
                  <div className="span2"><h3>操作</h3></div>
              </div>
				{Myaddress}
				</div>
                <a className="btn btn-link" href={"order#/"+this.props.order.id+"/payConfirm"} onClick={this.setTransAdress}>确认订单</a>

			</div>
		)
	}
})
