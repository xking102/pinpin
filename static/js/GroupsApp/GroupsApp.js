var React = require('react');
var GroupItem = require('./GroupItem'); 
var Pager =  require("./Pager");


module.exports = React.createClass({
	getInitialState:function(){
		var groups = [
			{
				id: 1,
				img: '/static/imgs/2.png',
				title:'#1新一轮日亚化妆品海淘开始，姐妹们快快加入xingkaixin你很厉害啊吧新一轮日',
				amount: 12,
				unit_price: 137,
				create_dt: 1231232333,
			}
			
		];

		return {
			groups: [],
			page: 1,
			pages: 1,
			pager_display: false
		}
	},
	listGroups:function(){
		var data = {
			page : 1
		};

		$.ajax({
            type:'get',
            url:'/api/v1/groups',
            data:data
        }).done(function (resp) {
        	if(resp.status == 201){
        		this.setState({
            		groups:resp.groups,
            		pager_display:true
            	});
        	}
        	else{
        		this.setState({
            		groups:[],
            		pager_display:false

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
			pager_display : this.state.pager_display
		};
		return (
			<div>
				<div>{groupComps}</div>
				<div className='col-md-12'>
					<div className='col-md-offset-5'><Pager {...pager_props}/></div>
				</div>
			</div>

		)
	}
})



