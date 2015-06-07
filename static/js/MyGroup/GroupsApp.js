var React = require('react');

var GroupItem = require('./GroupItem');
var Pager =  require("../Components/Pager");


module.exports = React.createClass({
	getInitialState:function(){
		return {
			groups: [],
			pager:[]
		}
	},
	listGroups:function(per,page){
		$.ajax({
            type:'get',
            url:'/api/v1/u/groups',
            datetype:'json',
            data:{
            	'per':per,
            	'page':page
            },
        	success:function (resp) {
        		this.setState({
            			groups:resp.groups,
            			pager:resp.pager
            		});
        	}.bind(this),
        	error:function(){
        		console.error(status, err.toString);
        	}.bind(this)
    	});
	},
	changeGroupStatus:function(groupid,status){
		var groups = this.state.groups;
		var update = React.addons.update;
		var group = groups.filter(function(group){
			return group.id == groupid;
		})[0];
		var index = groups.indexOf(group);
		var updategroup = update(group,{status:{$set:status}});
		var newgroups = update(groups,{
			$splice: [[index,1,updategroup]]
		});
		this.setState({
			groups:newgroups
		})
	},
	onNextPage:function(){
		this.listGroups(this.state.pager.per,this.state.pager.page+1);
	},
	onPrevPage:function(){
		this.listGroups(this.state.pager.per,this.state.pager.page-1);
	},
	componentDidMount : function(){
		this.listGroups(10,1);
	},
	componentWillReceiveProps  : function(){
		this.listGroups(10,1);
	},
	render:function(){
		var groups = this.state.groups;
		var groupComps = groups.map(function(item){
			return <GroupItem key={item.id}
							group={item} 
							listGroups={this.listGroups}
							changeGroupStatus={this.changeGroupStatus} />
		}.bind(this));
		var pager_props = {
			hasNext: this.state.pager.next,
			hasPrev: this.state.pager.prev,
			onClickNext : this.onNextPage,
			onClickPrev : this.onPrevPage
		};
		return (
			<div> 
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2><i className="halflings-icon user"></i><span className="break"></span>MyGroups</h2>	
					</div>

					<div className="box-content">
						<div className="row-fluid">
							{groupComps}		
						</div>
					</div>

					<div style={{marginBottom:'10px'}}>
					<Pager {...pager_props}/>
					</div>


					
				</div>
			</div>
			
    </div> 

		)
	}
})
