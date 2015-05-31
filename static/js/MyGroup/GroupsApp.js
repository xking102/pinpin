var React = require('react');

var GroupItem = require('./GroupItem');

var mui = require('material-ui');
var {Paper} = mui;

module.exports = React.createClass({
	getInitialState:function(){
		return {
			groups: []
		}
	},
	listGroups:function(){
		$.ajax({
            type:'get',
            url:'/api/v1/u/groups',
            datetype:'json',
        	success:function (resp) {
        		this.setState({
            			groups:resp.groups
            		});
        	}.bind(this),
        	error:function(){
        		console.error(status, err.toString);
        	}.bind(this)
    	});
	},
	componentDidMount : function(){
		this.listGroups();
	},
	componentWillReceiveProps  : function(){
		this.listGroups();
	},
	render:function(){
		var groups = this.state.groups;
		var groupComps = groups.map(function(item){
			return <GroupItem key={item.id}
							group={item}  />
		});
		return (
			<div> 
			<Paper zDepth={4}>
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2><i className="halflings-icon user"></i><span className="break"></span>MyGroups</h2>	
					</div>

					<div className="box-content">
						<div className="row-fluid">
									<div className="span3"><h3>名称</h3></div>
									<div className="span1"><h3>总数</h3></div>
									<div className="span1"><h3>下单未付款数</h3></div>
									<div className="span1"><h3>完成付款数</h3></div>
									<div className="span1"><h3>状态</h3></div>
									<div className="span3"><h3>行动</h3></div>
							</div>

							
								<div>{groupComps}</div>
							

					</div>


					
				</div>
			</div>
			</Paper>
    </div> 

		)
	}
})
