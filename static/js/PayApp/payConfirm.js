var React = require("react");
var mui = require('material-ui');
var PayItem = require('./PayItem');
var {Paper} = mui;

module.exports = React.createClass({
    getInitialState:function(){
        return {
            order: []
        }
    },
    listOrders:function(){
        $.ajax({
            type:'get',
            url:'/api/v1/orders/'+this.props.oid,
            datetype:'json'
        }).success(function (resp) {
            console.log(resp);
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
       
    return(
                <div className="row-fluid">
                    <PayItem order={this.state.order} />
                </div>

    )   
  }
})