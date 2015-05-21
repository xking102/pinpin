var React = require('react');
var GroupItem = require('./GroupItem'); 
var Pager =  require("./Pager");


module.exports = React.createClass({
	getInitialState:function(){
		return {
			groups: [],
			page: 1,
			pages: 1,
			pager_display: false,
			query_flag:'',
			button_name:'这里以后放分页'
		}
	},
	listGroups:function(){
		var data = {
			page : 2
		};
		this.setState({
            		query_flag:'yes',
            		button_name:'加载中'
            	});
		$.ajax({
            type:'post',
            url:'/api/v1/groups',
            data:data
        }).done(function (resp) {
        	console.log(resp);
        	if(resp.status === 200){
        		this.setState({
            		groups:resp.groups,
            		pager_display:true,
            		query_flag:'',
            		button_name:'这里以后放分页'
            	});
        	}
        	else{
        		this.setState({
            		groups:[],
            		pager_display:true,
            		query_flag:'',
            		button_name:'这里以后放分页'

            	});
        	}
            
                
        }.bind(this));

	},
	componentDidMount : function(){
		this.listGroups();
	},
	render:function(){
		var groups = this.state.groups;
		var groupComps = groups.map(function(item){
			return <GroupItem group={item}/>

		});
		var pager_props = {
			listGroups : this.listGroups,
			pager_display : this.state.pager_display,
			query_flag : this.state.query_flag,
			button_name : this.state.button_name
		};
		return (
			<div>
				<div className="row-fluid hideInIE8 circleStats">{groupComps}</div>
				<div className='row-fluid'>
					<div><Pager {...pager_props}/></div>
				</div>
			</div>

		)
	}
})



