var React = require('react');
var PayItems = require('./PayItems');


module.exports = React.createClass({
	getInitialState:function(){
		return {
			order: []
		}
	},
	listOrders:function(){
		$.ajax({
            type:'get',
            url:'/api/v1/orders/'+ this.props.oid,
            datetype:'json'
        }).done(function (resp) {
        	this.setState({
            		order:resp.order
            	});
        }.bind(this));
	},
	componentDidMount : function(){
		this.listOrders();
	},
	componentWillReceiveProps  : function(){
		this.listOrders();
	},
	render:function(){
		return (
			<div className="row-fluid">		
				<div><PayItems order={this.state.order} /></div>
			</div>

		)
	}
})
