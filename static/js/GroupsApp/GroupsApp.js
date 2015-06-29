var React = require('react');

var GroupItem = require('./GroupItem');

var injectTapEventPlugin = require("react-tap-event-plugin");
var mui = require('material-ui');
var RaisedButton = mui.RaisedButton;
var AppBar = mui.AppBar;
var ThemeManager = require('material-ui/lib/styles/theme-manager')();
var Colors = require('material-ui/lib/styles/colors');
var {Tabs, Tab, CircularProgress} = mui;
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
			pager:[],
			per: 16,
			page: 1,
			pager_display: false,
			query_flag:false,
			button_name:'这里以后放分页'
		}
	},
	listGroups:function(per,page){
		this.setState({
            		query_flag:true,
            		button_name:'加载中'
            	});
		$.ajax({
            type:'get',
            url:'/api/v1/groups',
            contentType: "application/json",
            data:{
            	'per':per,
            	'page':page

            },
            success:function(resp){
            	var finalGroups = resp.groups.map(function(group){
            		this.appendGroup( group );
            	}.bind(this));
            	this.setState({
            		//groups:resp.groups,
            		pager:resp.pager,
            		pager_display:true,
            		query_flag:false,
            		button_name:'这里以后放分页'
            	})
            }.bind(this),
            error: function(xhr, status, err) {
        		console.error(status, err.toString);
      		}.bind(this)
        });

	},
	appendGroup:function( newGroup ){
		var newGroups =  this.state.groups.concat( newGroup );
		this.setState({
			groups:newGroups
		})
	},
	onNextPage:function(){
		this.listGroups(this.state.pager.per,this.state.pager.page+1);
	},
	onPrevPage:function(){
		this.listGroups(this.state.pager.per,this.state.pager.page-1);
	},
	componentDidMount : function(){
		this.listGroups(this.state.per,this.state.page);
      	window.addEventListener('scroll', this.handleScroll);
	},
	componentWillUnmount: function() {
		window.removeEventListener('scroll', this.handleScroll);
	},
	handleScroll: function(event) {
		var scrollTop = this._getScrollTop();
		var clientHeight = this._getClientHeight();
		var scrollHeight = this._getScrollHeight();
    	if(scrollTop+clientHeight===scrollHeight){
    		if(this.state.query_flag){
    		}else{
    			if(this.state.pager.next){
    				this.listGroups(this.state.pager.per,this.state.pager.page+1);
    			}

    		}

    	}
	},
	_getScrollTop:function(){
		var scrollTop = 0;
		if(document.documentElement && document.documentElement.scrollTop){
			scrollTop = document.documentElement.scrollTop;
		}else if(document.body){
			scrollTop = document.body.scrollTop;
		}
		return scrollTop;
	},
	_getClientHeight:function(){
		var clientHeight = 0;
		if(document.body.clientHeight && document.documentElement.clientHeight){
			clientHeight = Math.min(document.body.clientHeight,document.documentElement.clientHeight);
		}else{
			clientHeight = Math.max(document.body.clientHeight,document.documentElement.clientHeight);
		}
		return clientHeight;
	},
	_getScrollHeight:function(){
		return Math.max(document.body.scrollHeight,document.documentElement.scrollHeight);
	},
	render:function(){
		var groups = this.state.groups;
		var	times = 0;
		var groupComps = groups.map(function(item){
			if(times>this.state.per-1){
				times = 0;
			}else{
				times +=1;
			}
			var delay = times*50;
			return <GroupItem key={item.id}
							group={item}
							delay={delay} />

		}.bind(this));

		var renew = this.state.query_flag?
		<div style={{marginLeft:'44%'}}><CircularProgress mode="indeterminate" /></div>:
		<div/>
		return (
			<div>
				<div>{groupComps}</div>
				{renew}

			</div>

		)
	}
})



