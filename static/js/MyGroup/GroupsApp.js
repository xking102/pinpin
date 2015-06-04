var React = require('react');

var GroupItem = require('./GroupItem');



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
							group={item} listGroups={this.listGroups} />
		});
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


					
				</div>
			</div>
			
    </div> 

		)
	}
})
