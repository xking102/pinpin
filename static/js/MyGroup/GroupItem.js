var React = require("react");

var mui = require('material-ui');
var {Paper} = mui;

var GroupItemNumDesc = require("./GroupItemNumDesc");
var GroupItemActions = require('./GroupItemActions');

module.exports = React.createClass({
    
    render:function(){
		return(
			<div style={{marginBottom:'15px'}}>
                <Paper zDepth={3}>
                    <div className="row-fluid" style={{marginLeft:'10px'}}>
                        <p>{this.props.group.title}</p>
                    </div>

                    <div className="row-fluid" style={{marginLeft:'10px',paddingBottom:'10px'}}>
                        <div className="span4">
                        <img alt="221x125" src="/static/imgs/groups/221x125.gif" />
                        </div>
                        
                        <div className="span4">
                        <GroupItemNumDesc group={this.props.group} />
                        </div>

                        <div className="span4">
                        <GroupItemActions group={this.props.group} 
                            listGroups={this.props.listGroups}
                            changeGroupStatus={this.props.changeGroupStatus} />
                        </div>
                    </div>
                </Paper>
            </div>

		)		
	}
})