var React = require('react');

var OrderItem = require('./OrderItem');
var Pager =  require("../Components/Pager");

module.exports = React.createClass({
	getInitialState:function(){
		return {
			orders: [],
			pager:[]
		}
	},
    changeOrderStatus:function(oid,status){
        var orders = this.state.orders;
        var update = React.addons.update;
        var order = orders.filter(function(order){
            return order.id == oid;
        })[0];
        var index = orders.indexOf(order);
        var updateorder = update(order,{status:{$set:status}});
        var neworders = update(orders,{
            $splice: [[index,1,updateorder]]
        });
        this.setState({
            orders:neworders
        })
    },
	listOrders:function(per,page){
		$.ajax({
            type:'get',
            url:'/api/v1/u/orders',
            datetype:'json',
            data:{
            	'per':per,
            	'page':page
            },
        	success:function (resp) {
        		this.setState({
            			orders:resp.orders,
            			pager:resp.pager
            		});
        	}.bind(this),
        	error:function(){
        		console.error(status, this.state.pager.e);
        	}.bind(this)
    	});   
	},
	componentDidMount : function(){
		this.listOrders(10,1);
	},
	componentWillReceiveProps  : function(){
		this.listOrders(10,1);
	},
	onNextPage:function(){
		this.listOrders(this.state.pager.per,this.state.pager.page+1);
	},
	onPrevPage:function(){
		this.listOrders(this.state.pager.per,this.state.pager.page-1);
	},
	render:function(){
		var orders = this.state.orders;
		var orderComps = orders.map(function(item){
			return <OrderItem key={item.id}
							order={item}
							changeOrderStatus={this.changeOrderStatus} />
		}.bind(this));
		var pager_props = {
			hasNext: this.state.pager.next,
			hasPrev: this.state.pager.prev,
			onClickNext : this.onNextPage,
			onClickPrev : this.onPrevPage
		};
		return (
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2><i className="halflings-icon user"></i><span className="break"></span>全部订单</h2>	
					</div>

					<div className="box-content">
						<div className="row-fluid">
									<div className="span2"><h3>订单编号</h3></div>
									<div className="span2"><h3>购买数量</h3></div>
									<div className="span2"><h3>订单金额</h3></div>
									<div className="span2"><h3>订单时间</h3></div>
									<div className="span2"><h3>订单状态</h3></div>
									<div className="span2"><h3>操作</h3></div>
							</div>

							
								<div>{orderComps}</div>
		
					</div>		
				</div>
				    <div style={{marginBottom:'10px'}}>
                    <Pager {...pager_props}/>
                    </div>
			</div>

		)
	}
})
