var React = require('react');
var GroupItem = require('./GroupItem'); 
var Pager =  require("../Components/Pager");

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
			pager:[],
			per: 1,
			page: 1,
			pager_display: false,
			query_flag:'',
			button_name:'这里以后放分页'
		}
	},
	listGroups:function(per,page){
		this.setState({
            		query_flag:'yes',
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
            	this.setState({
            		groups:resp.groups,
            		pager:resp.pager,
            		pager_display:true,
            		query_flag:'',
            		button_name:'这里以后放分页'
            	})
            }.bind(this),
            error: function(xhr, status, err) {
        		console.error(status, err.toString);
      		}.bind(this)
        });

	},
	onNextPage:function(){
		this.listGroups(this.state.pager.per,this.state.pager.page+1);
	},
	onPrevPage:function(){
		this.listGroups(this.state.pager.per,this.state.pager.page-1);
	},
	componentDidMount : function(){
		this.listGroups(8,1);
      	window.addEventListener('scroll', this.handleScroll);
	},
	componentWillUnmount: function() {
		window.removeEventListener('scroll', this.handleScroll);
	},
	handleScroll: function(event) {
    	var scrollTop = event.srcElement.body.scrollTop,
    	    itemTranslate = Math.min(0, scrollTop/3 - 60);
	
    	if(itemTranslate===0){
    		console.log('gotoBottom');
    	}
	},
	render:function(){
		var groups = this.state.groups;
		var groupComps = groups.map(function(item){
			return <GroupItem key={item.id} 
							group={item}/>

		});
		var pager_props = {
			hasNext: this.state.pager.next,
			hasPrev: this.state.pager.prev,
			onClickNext : this.onNextPage,
			onClickPrev : this.onPrevPage
		};
		return (
			<div ref="nav">
				<div className="row-fluid hideInIE8 circleStats">{groupComps}</div>
				<div className='row-fluid'>
					<div><Pager {...pager_props}/></div>
				</div>
			</div>

		)
	}
})



