var React = require("react");


module.exports = React.createClass({
    getInitialState : function(){
        return{
            reqnum : 1,
            btn_buy_name: '购买',
            query_flag: false
        }    
    },
    handlerReqnum:function(e){
        var newval  = e.target.value;
        if(newval > 0){
            if(newval<=this.props.group.total_qty){
                this.setState({
                    reqnum : parseInt(newval)
                })
            }
        }
    },
    handlerOrder:function(e){
        if(this.state.query_flag){
            console.log('waiting');
        }else{
          this.setState({
              btn_buy_name:'稍等',
              query_flag: true
          });
          $.ajax({
              type:'post',
              url:'/api/v1/orders',
              contentType: "application/json",
              data:JSON.stringify({
                'gid':this.props.group.id,
                'req_qty':this.state.reqnum,
                'unit_price':this.props.group.unit_price,
                'total_price':this.props.group.unit_price*this.state.reqnum,
                'actual_price':this.props.group.unit_price*this.state.reqnum,
                'actual_transfer_fee':0
              })
          }).success(function (resp) {
              this.setState({
                      btn_buy_name:'成功',
                      query_flag: false,
                  });
              window.location.href='/u/order#/'+resp.oid+'/pay';
          }.bind(this))
          .error(function (resp){
            this.setState({
                      btn_buy_name:'失败',
                      query_flag: false
  
                  });
          }.bind(this));
          }  
      },
  componentDidMount: function() {
    if($('.timeline')) {
    
        $('.timeslot').each(function(){
          
          var timeslotHeight = $(this).find('.task').outerHeight();
          
          $(this).css('height',timeslotHeight);
          
        });
    
    }
  },
  render:function(){
    var group = this.props.group;
    var styleObj={
            width: '45px',
        };
    return(
    <div>
  
  <div className="row-fluid">
    
    <div className="span7 noMarginRight">
      
      <div className="row-fluid">
        <div className="box span7">
          <div className="box-header" data-original-title>
            <h2>
            <i className="halflings-icon picture"></i>
            <span className="break"></span>
            {group.title}</h2>
          </div>
          
          <div className="box-content">
            <img className="grayscale" src="/static/imgs/groups/2.png" alt="Sample Image 1"/>
          </div>
          
        </div>
        <div className="box span5 noMarginRight">
          
          <div className="box-header" data-original-title>
            <h2>
            <i className="halflings-icon list-alt"></i>
            <span className="break"></span>
            购买信息</h2>
          </div>
          
          <div className="box-content">
            <h3>到手价：{group.unit_price}</h3>
            <h3>原价：{group.list_price}</h3>
            <h3>剩余数：{group.total_qty}</h3>
            <div className="row-fluid">
              
              <div className="span2">
                <input  style={styleObj} type="number" value={this.state.reqnum} onChange={this.handlerReqnum} />
              </div>
              
              <div className="span2">
                <a href="#" onClick={this.handlerOrder} className="btn btn-danger">{this.state.btn_buy_name}</a>
              </div>
              
            </div>
            
          </div>
          
        </div>
      </div>
      <div className="row-fluid">
        <div className="box span12">
          <div className="box-header" data-original-title>
            <h2>
            <i className="halflings-icon book"></i>
            <span className="break"></span>
            详细描述</h2>
          </div>
          
          <div className="box-content">
            {group.desc}
          </div>
          
        </div>
      </div>
    </div>
    <div className="span5 noMarinLeft">
      <div className="dark">
        
        <h1>Timeline</h1>
        
        <div className="timeline">
          <div className="timeslot">
            
            <div className="task">
              <span>
                <span className="type">appointment</span>
                <span className="details">
                  Dennis Ji at Bootstrap Metro Dashboard HQ
                </span>
                <span>
                  remaining time
                  <span className="remaining">
                    3h 38m 15s
                  </span>
                </span>
              </span>
              <div className="arrow"></div>
            </div>
            <div className="icon">
              <i className="icon-map-marker"></i>
            </div>
            <div className="time">
              3:43 PM
            </div>
            
          </div>
          
          <div className="clearfix"></div>
          <div className="timeslot alt">
            
            <div className="task">
              <span>
                <span className="type">phone call</span>
                <span className="details">
                  Dennis Ji
                </span>
                <span>
                  remaining time
                  <span className="remaining">
                    3h 38m 15s
                  </span>
                </span>
              </span>
              <div className="arrow"></div>
            </div>
            <div className="icon">
              <i className="icon-phone"></i>
            </div>
            <div className="time">
              3:43 PM
            </div>
            
          </div>
          <div className="timeslot">
            
            <div className="task">
              <span>
                <span className="type">mail</span>
                <span className="details">
                  Dennis Ji
                </span>
                <span>
                  remaining time
                  <span className="remaining">
                    3h 38m 15s
                  </span>
                </span>
              </span>
              <div className="arrow"></div>
            </div>
            <div className="icon">
              <i className="icon-envelope"></i>
            </div>
            <div className="time">
              3:43 PM
            </div>
            
          </div>
          
          <div className="timeslot alt">
            
            <div className="task">
              <span>
                <span className="type">deadline</span>
                <span className="details">
                  Fixed bugs
                </span>
                <span>
                  remaining time
                  <span className="remaining">
                    3h 38m 15s
                  </span>
                </span>
              </span>
              <div className="arrow"></div>
            </div>
            <div className="icon">
              <i className="icon-calendar"></i>
            </div>
            <div className="time">
              3:43 PM
            </div>
            
          </div>
          
          <div className="timeslot">
            
            <div className="task">
              <span>
                <span className="type">appointment</span>
                <span className="details">
                  Dennis Ji at Bootstrap Metro Dashboard HQ
                </span>
                <span>
                  remaining time
                  <span className="remaining">
                    3h 38m 15s
                  </span>
                </span>
              </span>
              <div className="arrow"></div>
            </div>
            <div className="icon">
              <i className="icon-map-marker"></i>
            </div>
            <div className="time">
              3:43 PM
            </div>
            
          </div>
          
          <div className="clearfix"></div>
          
        </div>
      </div>
    </div>
  </div>
  
</div>
    )   
  }
})