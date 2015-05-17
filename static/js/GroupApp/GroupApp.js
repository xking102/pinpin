var React = require('react');
var GroupItem = require('./GroupItem'); 



module.exports = React.createClass({
	contextTypes: {
    	router: React.PropTypes.func.isRequired
  	},
	getInitialState:function(){
		return {
			groups: [],
			query_flag:'',
			button_name:'这里以后放分页'
		}
	},
	listGroups:function(){
    	var params = this.context.router.getCurrentParams();
    	var gid = params.gid;
		this.setState({
            		query_flag:'yes',
            		button_name:'加载中'
            	});
		$.ajax({
            type:'get',
            url:'/api/v1/groups/'+ gid,
        }).done(function (resp) {
        	if(resp.status == 201){
        		this.setState({
            		groups:resp.groups,
            		query_flag:'',
            		button_name:'这里以后放分页'
            	});
        	}
        	else{
        		this.setState({
            		groups:[],
            		pager_display:false,
            		query_flag:'',
            		button_name:'这里以后放分页'

            	});
        	}
            
                
        }.bind(this));

	},
	componentDidMount : function(){
		this.listGroups();
	},
	componentWillReceiveProps  : function(){
		this.listGroups();
	},
	render:function(){
		var group_props = {
			listGroups : this.listGroups,
			pager_display : this.state.pager_display,
			query_flag : this.state.query_flag,
			button_name : this.state.button_name,
			group : this.state.groups
		};
		return (
			<div>
				<GroupItem {...group_props}/>
			</div>

		)
	}
})



