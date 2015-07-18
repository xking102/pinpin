var React = require("react");
var AMUIReact = require('amazeui-react');
var {ScrollSpy} = AMUIReact;

var mui = require('material-ui');
var {Card, CardMedia, CardTitle, CardText, Paper} = mui;

module.exports = React.createClass({
    contextTypes: {
        router: React.PropTypes.func.isRequired
    },
    getInitialState:function(){
        return {
            depth:1
        }
    },
    MouseIn:function(){
        this.setState({
            depth:3
        });
    },
    MouseOut:function(){
        this.setState({
            depth:1
        });
    },
    _handleClick:function(){
        this.context.router.transitionTo('group', {gid: this.props.group.id});
    },
	render:function(){
		var group = this.props.group;
        var title = group.title;
        if(title){
            if(title.length>9){
                title = title.substring(0,9)+'...';
            }
        }
		return(
            <div>
            <a href="javascript:void(0)" onClick={this._handleClick}>
			<div className="span3"
                style={{marginBottom:'20px',marginRight:'20px'}}
                onMouseEnter={this.MouseIn} onMouseLeave={this.MouseOut}>

            <Paper zDepth={this.state.depth}>
            <ScrollSpy norepeat animation="slide-bottom" delay={this.props.delay}>

                <Card>
                    <CardMedia overlay={
                        <CardTitle title={title} />
                    }>
                        <img  src={group.image+'.small.jpg'}/>
                    </CardMedia>

                    <CardText>
                        <p>到手价：￥ {group.unit_price}</p>
                        <p>剩余数量：{group.total_qty-group.req_qty-group.confirm_qty}</p>
                        <p>发布时间：{group.create_dt}</p>
                    </CardText>
                </Card>


            </ScrollSpy>
            </Paper>
			</div>
            </a>
            </div>

		)
	},

})
