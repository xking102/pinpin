var React = require('react');
var GroupItem = require('./GroupItem'); 
var Pager =  require("./Pager");

var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var RaisedButton = mui.RaisedButton;
var AppBar = mui.AppBar;
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');
var {Tabs, Tab} = mui;
var Typography = mui.Styles.Typography;


injectTapEventPlugin();
module.exports = React.createClass({
	childContextTypes: {
    	muiTheme: React.PropTypes.object
  	},
  	getChildContext: function() {
    	return {
    	  muiTheme: ThemeManager.getCurrentTheme()
    	};
 	},
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
            type:'get',
            url:'/api/v1/groups',
            data:data
        }).done(function (resp) {
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
			return <GroupItem key={item.id} 
							group={item}/>

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



